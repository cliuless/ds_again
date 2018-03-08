
Lets see how we would 'dummify' our categorical features in Spark.

Reattach to your spark docker container from yesterday.
Launch a new Jupyter Notebook


1) Get Mushroom data:
 using wget or scp..
# https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names

2) read in the data with spark DataFrame

& Rename column names :
columns=["edible","cap_shape","cap_surface","cap-color", "bruises","odor","gill_attachment",
         "gill_spacing","gill_size","gill_color","stalk_shape","stalk-root","stalk_surface_above_ring",
        "stalk_surface_below_ring","stalk_color_above_ring",
         "stalk_color_below_ring","veil_type","veil_color","ring_number","ring_type",
         "spore_print_color","population","habitat"]

3) We have a heck of lot of dummy variables for this dataset; 
Transform data to dummy variables .. Use pipeline implementation.

Hint: see https://spark.apache.org/docs/2.1.0/ml-features.html#stringindexer
Hint Hint: you might have to google around a bit too.
