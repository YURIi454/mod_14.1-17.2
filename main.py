from config import PATH_JSON
from src.class_category import Category
from src.class_product import Product
from src.file_handler import create_obj_from_json, read_json

if __name__ == "__main__":
    result = create_obj_from_json(read_json(PATH_JSON))
    print(result[0][0].name)
    print(result[0][0].description)
    print()
    print(result[1][0].name)
    print(result[1][0].description)
    print(result[1][0].price)
    print(result[1][0].quantity)
    print()
    print(result[1][1].name)
    print(result[1][1].description)
    print(result[1][1].price)
    print(result[1][1].quantity)
    print()
    print(result[1][2].name)
    print(result[1][2].description)
    print(result[1][2].price)
    print(result[1][2].quantity)
    print()
    print(result[0][1].name)
    print(result[0][1].description)
    print(result[1][3].name)
    print(result[1][3].description)
    print(result[1][3].price)
    print(result[1][3].quantity)
    print()
