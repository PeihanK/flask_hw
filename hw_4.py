from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship('Category', back_populates='products')


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    products = relationship('Product', back_populates='categories')


Base.metadata.create_all(engine)


# добавление категорий
def add_categories(session):
    categories = [
        Category(name="Электроника", description="Гаджеты и устройства."),
        Category(name="Книги", description="Печатные книги и электронные книги."),
        Category(name="Одежда", description="Одежда для мужчин и женщин.")
    ]
    session.add_all(categories)
    session.commit()
    return categories


# добавление продуктов
def add_products(session):
    electronics = session.query(Category).filter_by(name="Электроника").first()
    books = session.query(Category).filter_by(name="Книги").first()
    clothing = session.query(Category).filter_by(name="Одежда").first()

    products = [
        Product(name="Смартфон", price=299.99, in_stock=True, categories=electronics),
        Product(name="Ноутбук", price=499.99, in_stock=True, categories=electronics),
        Product(name="Научно-фантастический роман", price=15.99, in_stock=True, categories=books),
        Product(name="Джинсы", price=40.50, in_stock=True, categories=clothing),
        Product(name="Футболка", price=20.00, in_stock=True, categories=clothing)
    ]
    session.add_all(products)
    session.commit()


# обновление цены смартфона
def upd_smartphone_price(sync_session):
    with sync_session() as session:
        smartphone = session.query(Product).filter(Product.name == "Смартфон").first()
        if smartphone:
            smartphone.price = 349.99
            session.commit()
            print(f'New price of "Смартфон": {smartphone.price}')
        else:
            print('"Смартфон" not found')


# подсчет продуктв в категориях
def count_products_by_category(sync_session):
    with sync_session() as session:
        by_category_counts = session.query(
            Category.name, func.count(Product.id).label('product_count')
        ).join(Product).group_by(Category.id).all()
        return by_category_counts


# вывод всех продуктов и категорий
def product_and_categories(session):
    all_categories = session.query(Category).all()
    all_products = session.query(Product).all()

    print("Категории:")
    for category in all_categories:
        print(f"Название: {category.name}, Описание: {category.description}")

    print("\nПродукты:")
    for product in all_products:
        print(
            f"Название: {product.name}, Цена: {product.price}, "
            f"В наличии: {product.in_stock}, Категория: {product.categories.name}")


# вывод кол-ва продуктов в категориях
def category_count(by_category_counts):
    print("\nКолличество продуктов в категории:")
    for category_name, count in by_category_counts:
        print(f'{category_name}: {count}')


# фильтрация категорий, где больше 1 продукта
def filter_more_than_one_product(sync_session):
    with sync_session() as session:
        filtered_categories = session.query(
            Category.name, func.count(Product.id).label('product_count')
        ).join(Product).group_by(Category.id).having(func.count(Product.id) > 1).all()
        return filtered_categories


# вывод категорий, где больше 1 продукта
def print_more_than_one_product(filtered_categories):
    print('\nКатегории, в которых количество продуктов больше 1:')
    for category_name, count in filtered_categories:
        print(f'{category_name}: {count}')


# запуск
with Session() as session:
    add_categories(session)
    add_products(session)
    upd_smartphone_price(Session)
    product_and_categories(session)
    by_category_counts = count_products_by_category(Session)
    category_count(by_category_counts)
    filtered_categories = filter_more_than_one_product(Session)
    print_more_than_one_product(filtered_categories)
