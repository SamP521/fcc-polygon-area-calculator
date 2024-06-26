class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width_set):
        self.width = width_set
    
    def set_height(self, height_set):
        self.height = height_set
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        picture = '*' * self.width + '\n'
        picture = picture * self.height
        
        return picture
    
    def get_amount_inside(self, other_shape):
        return (self.height // other_shape.height) * (self.width // other_shape.width)

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.width = side 
        Rectangle.height = side 
    
    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.height = side
        self.width = side
