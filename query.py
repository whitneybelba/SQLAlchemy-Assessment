"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# # Get the brand with the **id** of 8.
Brand.query.get(8)

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
models = Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# # Get all models that are older than 1960.
models = Model.query.filter(Model.year < 1960).all()

# # Get all brands that were founded after 1920.
brands = Brand.query.filter(Brand.founded > 1920).all()

# # Get all models with names that begin with "Cor".
models = Model.query.filter(Model.name.like('Cor%')).all()

# # Get all brands that were founded in 1903 and that are not yet discontinued.
brands = Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued == None)).all()

# # Get all brands that are either 1) discontinued (at any time) or 2) founded
# # before 1950.
brands = Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# # Get any model whose brand_name is not Chevrolet.
models = Model.query.filter(Model.brand_name != "Chevrolet").all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter_by(year=year).all()

    for model in models:
        print "Model Name: %s \t Brand Name: %s \t Headquarters: %s \n" % (
            model.name, model.brand_name, model.brand.headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    models = Model.query.all()

    for model in models:
        print "Model Name: %15s \t \t Brand Name: %15s \n" % (
            model.name, model.brand_name)

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# ANSWER: <flask_sqlalchemy.BaseQuery object at 0x7fd3911a3b10> is the returned
# value - it's datatype is a query object.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# ANSWER: An association table is a table whose main purpose is to link/glue two
# other tables together. There are no meaningful fields/data in an association
# table - it is there just make a relationship exist between two tables with meaningful
# data. Association tables manage many to many relationships.

# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):
    '''Returns a list of objects that are brands whose name contains
    or is equal to the input string.'''

    brands = Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()

    return brands


def get_models_between(start_year, end_year):
    '''Takes in a start year and end year as integers, and returns a list
    of objects that are models with years that fall between the start year
    (inclusive) and end year (exclusive).'''

    models = Model.query.filter(Model.year > (start_year - 1),
                                Model.year < end_year).all()

    return models
