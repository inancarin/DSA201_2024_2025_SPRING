class Rectangle:
    def __init__(self, x_left, y_left, x_right, y_right):
        self.x_left = x_left
        self.y_left = y_left
        self.x_right = x_right
        self.y_right = y_right
        self.height = y_right - y_left
        self.width = x_right - x_left
    
    def __str__(self):
        res = "*" * self.width + "\n"
        for i in range(self.height-2):
            temp = "*" + " " *( self.width-2) + "*\n"
            res += temp
        temp = "*" * self.width + "\n"
        res += temp
        
        return res

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)
    