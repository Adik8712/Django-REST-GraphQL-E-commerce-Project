import graphene
from graphene_django import DjangoObjectType

from main.models import Category, News, Product


# Работает как serializers
class CategoryModelType(DjangoObjectType):
    class Meta:
        model = Category

class ProductModelType(DjangoObjectType):
    class Meta:
        model = Product

class NewsModelType(DjangoObjectType):
    class Meta:
        model = News

# Работает как viewset
class Query(graphene.ObjectType):
    category_model = graphene.List(CategoryModelType)
    product_model = graphene.List(ProductModelType)
    news_model = graphene.List(NewsModelType)

    def resolve_category_model(self, info):
        return Category.objects.all()
    
    def resolve_product_model(self, info):
        return Product.objects.all()

    def resolve_news_model(self, info):
        return News.objects.all()


# _______________________________________________________
class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    
    category = graphene.Field(CategoryModelType)

    def mutate(self, info, name):
        category = Category.objects.create(name=name)
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    category = graphene.Field(CategoryModelType)

    def mutate(self, info, id, name=None):
        category = Category.objects.get(id=id)

        if name:
            category.name = name

        category.save()
        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()

    def mutate(self, info, id):
        category = Category.objects.get(id=id)
        if category:
            category.delete()
            return DeleteCategory(success=True)
        else:
            return DeleteCategory(success=False)

# __________________________________________________
class CreateProduct(graphene.Mutation):
    class Arguments:
        image = graphene.String(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Int(required=True)
        category_id = graphene.Int(required=True) # 4

    product = graphene.Field(ProductModelType)

    def mutate(self, info, image, name, description, price, category_id):
        category = Category.objects.get(id=category_id) # Food
        product = Product.objects.create(image=image, name=name, 
                        description=description, price=price, category=category)
        
        return CreateProduct(product=product)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        image = graphene.String()
        name = graphene.String()
        description = graphene.String()
        price = graphene.Int()
        category_id = graphene.Int()

    product = graphene.Field(ProductModelType)

    def mutate(self, info, id, image=None, name=None, 
            description=None, price=None, category_id=None):
        product = Product.objects.get(id=id)

        if image:
            product.image = image
        if name:
            product.name = name
        if description:
            product.description = description
        if price:
            product.price = price
        if category_id:
            category = Category.objects.get(id=category_id)
            product.category = category

        product.save()
        return UpdateProduct(product=product)


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()

    def mutate(self, info, id):
        product = Product.objects.get(id=id)
        if product:
            product.delete()
            return DeleteProduct(success=True)
        else:
            return DeleteProduct(success=False)

# __________________________________________________

class CreateNews(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    news = graphene.Field(NewsModelType)

    def mutate(self, info, title, description):
        news = News.objects.create(title=title, description=description)
        
        return CreateNews(news=news)


class UpdateNews(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()

    news = graphene.Field(NewsModelType)

    def mutate(self, info, id, title=None, description=None):
        news = News.objects.get(id=id)

        if title:
            news.title = title
        if description:
            news.description = description

        news.save()
        return UpdateNews(news=news)
    

class DeleteNews(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()

    def mutate(self, info, id):
        news = News.objects.get(id=id)
        if news:
            news.delete()
            return DeleteNews(success=True)
        else:
            return DeleteNews(success=False)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field() # POST
    update_category = UpdateCategory.Field() # PUT
    delete_category = DeleteCategory.Field() # DELETE

    create_product = CreateProduct.Field() # POST
    update_product = UpdateProduct.Field() # PUT
    delete_product = DeleteProduct.Field() # DELETE

    create_news = CreateNews.Field() # POST
    update_news = UpdateNews.Field() # PUT
    delete_news = DeleteNews.Field() # DELETE

schema = graphene.Schema(query=Query, mutation=Mutation)