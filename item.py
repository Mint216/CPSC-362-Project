from decimal import Decimal, InvalidOperation

'''Item class for creating clothes'''

class Item():
    def __init__(self, category, type, name, price):
        self._category = category   # Ex: Pants, Shirts, Hats
        self._item_type = type      # Ex: Pants -> Jeans, Shorts, Sweats
        self._name = name           # Name of Item
        self._price = price         # Price of Item
        self._desc = "N/A"          # Description of Item

    '''
    Properties can be used like instance variables but are still private
    Can be used like:
    print(object.category)
    object.category = 'Pants'
    '''

    @property
    def category(self):
        '''Returns category'''
        return self._category

    @category.setter
    def category(self, category):
        '''Sets category of clothing'''
        # Can change to include other categories like shoes
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        if len(category) == 0:
            raise ValueError("category must include at least one character")
        if category in ('Pants', 'Shirts', 'Hats'):
            self._category = category
        else:
            raise ValueError("category must be Pants, Shirts, or Hats")

    @property
    def item_type(self):
        '''Returns type of item'''
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        '''Sets type of clothing item'''
        if not isinstance(item_type, str):
            raise TypeError("item type must be a string")
        if len(item_type) == 0:
            raise ValueError("item type must include at least one character")
        self._item_type = item_type

    @property
    def name(self):
        '''Returns name of item'''
        return self._type

    @name.setter
    def name(self, name):
        '''Sets name'''
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) == 0:
            raise ValueError("name must include at least one character")
        self._name = name

    @property
    def price(self):
        '''Returns price of item'''
        return self._price

    '''
    Decimal object is better for financial calculations
    Setter will take in a string, float, or int number and convert to Decimal obj
    '''
    @price.setter
    def price(self, price):
        '''Sets price as a Decimal'''
        try:
            decimal_price = Decimal(str(price))
        except (InvalidOperation, ValueError):
            raise TypeError("price must be a number (int, float, or string convertible to Decimal)")
        if decimal_price < 0:
            raise ValueError("price must not be a negative number")
        self._price = decimal_price

    @property
    def desc(self):
        '''Returns desc of item'''
        return self._desc

    @desc.setter
    def desc(self, desc):
        '''Sets name'''
        if not isinstance(desc, str):
            raise TypeError("desc must be a string")
        if len(desc) == 0:
            raise ValueError("desc must include at least one character")
        self._desc = desc