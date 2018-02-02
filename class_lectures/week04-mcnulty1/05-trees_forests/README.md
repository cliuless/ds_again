### Schedule

**9:00 am**: [Pair Problem](pair.md)

		Audrey, Chris
		Rishabh, Browning
		Jaydon, Mauro
		Sungwan, Laura
		Malik, Christine.C
		Wendy, Matias
		Brad.S, Kevin
		Pavan, Will
		Christine.L, Louisa
		Arina, Summer
		Adam, Brad.D
		Jit, Jon
		Jeremy, Brian

**10:30 am**: [Error metrics for classification](Classification_Errors.pdf)

**11:00 am**: [Decision Trees and Random Forests](Decision_Trees_Random_Forests.pdf)

**12:00pm**: Lunch

**1:00 pm**: 2 Investigation Presentations

**1:30 pm**: Work Time


### Reading

 * [Rutgers decision tree lecture](http://www.cs.rutgers.edu/~mlittman/courses/ml04/ch3.pdf) (some of our slides are based on this)
 * [Wisconsin decision tree lecture](http://pages.cs.wisc.edu/~jerryzhu/cs540/handouts/dt.pdf) (similar, more examples)
 * [Decision trees in sklearn](http://scikit-learn.org/stable/modules/tree.html) (including demo showing how to examine generated rules)
 * [Wikipedia entry on random forests](http://en.wikipedia.org/wiki/Random_forest)
 * [Wikipdia entry including information entropy](http://en.wikipedia.org/wiki/Entropy_%28information_theory%29)
 * [Using Python to build a decision tree from scratch](http://nbviewer.ipython.org/github/gumption/Python_for_Data_Science/blob/master/4_Python_Simple_Decision_Tree.ipynb)
 * A [notebook](http://nbviewer.ipython.org/gist/rcarneva/261dd7baa4a4a2a8bf2b) demonstrating gradient boosted trees, among other things.

 ### More on Error Metrics

 * [Precision, recall, sensitivity, specificity](http://uberpython.wordpress.com/2012/01/01/precision-recall-sensitivity-and-specificity/)
 * [Wikipedia page on precision and recall](http://en.wikipedia.org/wiki/Precision_and_recall)
 * [Scikit learn on classification metrics](http://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
 * [Receiver Operating Characteristic](http://gim.unmc.edu/dxtests/roc2.htm)
 * [Area under curve (ROC)](http://gim.unmc.edu/dxtests/roc3.htm)


##### What is the relationship between F1 and Fß?

If you have found the [metrics function](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html) in `sklearn` that spits out your precision, recall, and F score, you might have found yourself asking: "What is Fß? Is it the same as F1?"

The answer is ... yes. F1 combines precision and recall. Fß does
the same thing, but uses a weight so that you can weigh one of these
two (precision or recall) more than the other when combining them. It
is a way to tune your score if you care more about precision than
recall, for example. F1 is the Fß for which ß = 1. In
`sklearn`, the default value for ß is 1.

The [wikipedia page](http://en.wikipedia.org/wiki/F1_score) has more on this relationship.

#### More SVM
[nice video on Lagrangian multipliers](https://github.com/thisismetis/nyc18_ds14/edit/master/class_lectures/week04-mcnulty1/05-trees_forests/README.md)

[more on the optimization - video](https://www.youtube.com/watch?v=1aQLEzeGJC8)

[More SVMs (pg 337)](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf)

