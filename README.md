# BigData
These are the code instructions
Part c. Currency Conversion (3 Currencies)
Using selection statements, write a program to convert an amount of money from one currency to another.
The program should:
a. Ask the user to enter the amount of money;
b. Ask the user the current currency (one of USD, EUR, RMB);
c. Ask to which currency this amount should be converted (USD, EUR, or RMB);
d. Calculate the conversion using recent exchange rates;
e. Print the results to the user.
You can find recent exchange rates by Googling ‘x to y’ where x is the starting currency and y is the new
currency. For example, ‘EUR to USD’ will return something like ‘1 Euro equals 1.09 United States Dollar’.
Using if and elif statements, determine which conversion is appropriate. Use nested selection statements
for the maximum credit. You can use non-nested (parallel) selection statements to receive nearly full
credit (-2pts). If the user enters an unknown currency, print an error message. For your program, you can
use exchange rates fab in one direction, and infer the inverse direction fba as 1/fab. Alternatively, you
can look up and use both fab and fba. Real FX rates are like the latter case. For this assignment, you should
hard-code the exchange rates as part of the program. In practice, exchange rates would come into the
program from a database or real-time feed. Start your program with the comment #Firstname Lastname
Assignment2c and save the file named like LastnameFirstnameAsn2c.py
Your program should look similar to the example shown below.
Welcome to the 3-currency calculator!
Please enter the From amount: 100
Please enter the From currency (USD, EUR, or RMB): EUR
Please enter the To currency (USD, EUR, or RMB): USD
100.0 EUR equals 109.35 USD
