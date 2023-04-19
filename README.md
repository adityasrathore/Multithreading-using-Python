# Multithreading-using-Python


1) The code imports the necessary libraries and modules required to build a dashboard and generate random numbers.
2) The NUM_NUMBERS variable is set to 5, which determines the number of random numbers to generate.
3) The layout of the dashboard is defined using Dash's html and dcc modules. It consists of three columns, each with an html.Ul element that displays a list of random numbers.
4) The generate_random_numbers function generates random numbers and appends them to a list. It is called by each of the three callback functions.
5) The three callback functions are responsible for updating each of the three columns every 1, 2, and 3 seconds, respectively. They call the generate_random_numbers function using threading, which allows the function to be executed concurrently in a separate thread.
6) Each callback function waits for the generate_random_numbers function to complete by calling the join method on the thread. This ensures that the list of random numbers is fully populated before returning the updated list to the dashboard.
7) Finally, the dashboard server is started by calling app.run_server. <br>
The emphasis of this code is on the use of multithreading to generate random numbers. By using threading, the generate_random_numbers function can be executed concurrently in a separate thread, which allows the dashboard to remain responsive while the function is executing. The use of threading also ensures that the function is executed in a non-blocking way, so that the dashboard can continue to function as expected even if the function takes a long time to complete.
