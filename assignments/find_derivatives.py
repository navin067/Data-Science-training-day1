import sympy as sp
import time

class Find_derivatives:

      # defining the list of functions as a dictionary with id and function

      functions = {
            1 : "sin(x)",
            2 : "cos(x)",
            3 : "tan(x)",
            4 : "ln(x)",
            5 : "exp(ax)",
            6 : "x**n",
            7 : "g(x) + h(x)",
            8 : "g(x) * h(x)",
            9 : "g(x)/h(x)",
            10 : "g(h(x))",
      }

      def __init__(self):
            # initializing required symbols and functions
            self.x = sp.symbols('x')
            self.n = sp.symbols('n')
            self.a = sp.symbols('a')
            self.g = sp.Function('g')(self.x)
            self.h = sp.Function('h')(self.x)

      # defining the classmethod to access the function{} (dictionary)
      @classmethod
      def get_list_of_function(cls):
            return cls.functions

      #function to show the list of available functions to choose from
      def show_functions(self):
            print("\n\n ***** These are the list of functions available. ***** \n")
            function_list = self.get_list_of_function()
            for x, y in function_list.items():
                  print(f"Id: {x}       Function: {y}")
            return int(input("\nEnter the specific id of the function whose derivative you want to find out? "))

      # function defined to pass the id and respective function whose derivative is to be evaluated
      def select_function(self, choice):
            if(choice == 1):
                  self.generate_derivative(choice, sp.sin(self.x))
            elif(choice == 2):
                  self.generate_derivative(choice, sp.cos(self.x))
            elif(choice == 3):
                  self.generate_derivative(choice, sp.tan(self.x))
            elif(choice == 4):
                  self.generate_derivative(choice, sp.ln(self.x))
            elif(choice == 5):
                  self.generate_derivative(choice, sp.exp(self.a * self.x))
            elif(choice == 6):
                  self.generate_derivative(choice, self.x ** self.n)
            elif(choice == 7):
                  self.generate_derivative(choice, self.g + self.h)
            elif(choice == 8):
                  self.generate_derivative(choice, self.g * self.h)
            elif(choice == 9):
                  self.generate_derivative(choice, self.g / self.h)
            elif(choice == 10):
                  self.generate_derivative(choice, self.g.subs(self.x,self.h))
            else:
                  print("\n ----- You must only input ids (1 to 10) and select a particular function: -----")
                  new_choice = self.show_functions()
                  self.select_function(new_choice)

      #function defined to find the derivative and print it
      def generate_derivative(self,choice,function):
            dfdx = sp.diff(function,self.x)
            inquiry_function = self.get_list_of_function()
            print(f'\nFunction you chose is: {inquiry_function.get(choice)} whose derivative is: {dfdx}')

#creating the class object
first_derivative = Find_derivatives()

#prompting user the list of function asking to chose one particular function
choice = first_derivative.show_functions()

#evaluating start time
start_time = time.time()

#finding derivative
first_derivative.select_function(choice)

#evaluating end time
end_time = time.time()

#calculating execution time
execution_time = end_time - start_time
print(f'\nTime taken for the exection of the program is: "{execution_time}"')

