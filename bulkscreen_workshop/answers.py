class UnSolvedQuestionException(Exception):
  pass
class Answer():
  def __init__(self, answer_dict=ANSWER_DICT):
    self.answer_dict = answer_dict
  def show(self, Q_key, did_you_answer = False):
    if not did_you_answer:
      raise UnSolvedQuestionException("You haven't solved this question.")
    for k, ans in self.answer_dict[Q_key].items():
      print("{}:".format(k))
      print("\t{}\n".format(ans.replace("\n", "\n\t")))
    
ANSWER_DICT={
  "Q1":{
  "Q1_1":"Gini index of 0 means perfect equality of all guide counts.\nGini index of 1 means single guide takes up all read counts.",
  "Q1_2":"MAGeCK-VISPR recommends the Gini index should be <0.1 before \n"+\
  "selection and <0.2 after selection. However, in practice, this is not \n"+\
  "satisfied in decent quality screen. If the read depth is enough, moderate \n"+\
  "guide imbalance doesn't hinder the correct analysis.",
  "Q1_3":"T0 has the lowest Gini index, and it increases in the later time \n"+\
"point samples. This makes sense because as selection happens, cells with subset \n"+\
"of guides will be depleted in the later time points, increasing the imbalance."
  },
  "Q2":{
    "Q2_1":
    "T0 and T12A shows the lowest correlation with other samples, but only slightly. \n"+\
    "No samples show significantly low correlation so that it should be excluded.",
    "Q2_2":
    "T18C and T15C shows perfect correlation, which is not really plausible. If you check \n"+\
    "the raw reads above, you'll be able to find exactly same read counts. This is likely \n"+\
    "due to the sample mislabeling or error during preprocessing. We will use as is for now."
  },
  "Q3":{
    "Q3_1":
    "Perturbing essential gene will kill the cells, so the guides that target essential \n"+\
    "genes would be depleted in the later time point.",
    "Q3_2":
    "Yes. LFC is showing log(p_guide_T18/p_guide_T8) which should be negative when \n"+\
    "p_guide_T18 < p_guide_T8. So the essential genes should be enriched in negative \n"+\
    "LFC, which we can see in the plot.\n"+\
    "However, we're also observing some positive control guides with high LFC in the \n"+\
    "opposite direction."
  },
  "Q4":
  {"Q4_1":
   "In guide significance plot, there are lots of variant and negative control guides with \n"+\
   "highly significant p-values. However, in gene signifiance plot, most of the negative \n"+\
   "control and variant genes have very low significance.",
   "Q4_2":
   "MAGeCK-RRA measure gene significance based on whether the p-value of multiple guides targeting \n"+\
   "the gene (in this case, 5 guides per gene) is uniformly distributed or not. Based on the obser-\n"+\
   "vation, we can imagine that most guides with very significant p-values are of the gene where \n"+\
   "other guides that target the gene have moderate or low significance so that overall p-value \n"+\
   "ranks are uniformly distributed."
  },
  "Q5":
  {"Q5":"Yes. Note that this is not always true!"},
  
}
