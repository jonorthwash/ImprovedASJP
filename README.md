# Improved ASJP

Senior Thesis: Computational Model for Language Family Homeland Identification

The main purpose of this thesis is to examine possible improvements of the ASJP model, a computational model used for language family homeland identification. Historically, the homeland of a language family can be hypothesized with the linguistic comparative method, which requires considerable time, labor, and linguistic expertise. In that case, computational models are proposed as a complement for the linguistic approach to provide relatively objective, perspicacious results using a limited amount of raw data.

The ASJP model conjectures geographical origins of world’s language families through linguistic similarity and geographical distribution of languages within a language family (Wichmann et al. 2010). The model measures the linguistic distance of two languages as the normalized Levenshtein distance between semantically equivalent words in their Swadesh lists. It then computes the ratio between their linguistic distance and geographical distance as the diversity of the area that two languages span. Finally, the model uses the center of gravity principle to hypothesize possible homelands based on the diversity between commonly-spoken languages within the language family.

This thesis is aimed at modifying the oversimplistic methodology of the original ASJP model to incorporate more linguistic consideration. Specifically, while the original model uses naive Levenshtein distance as the measure for language distance, this thesis proposes to weigh the operations of Levenshtein distance by the frequencies for different sound changes to happen in natural languages. In this thesis, the frequencies will be set arbitrarily based on a priori knowledge, yet in future investigation they could be developed to be learned automatically through linguistic data.

The modified computational model will be implemented in python and tested on the well-studied Indo-European family. The results will be compared to the two major theories about the Proto-Indo-European homeland, the Steppe Theory and the Anatolian Hypothesis. The data is from Indo-European Lexical Cognacy Database (Dunn), which is consisted of 200-word Swadesh lists of more than 100 Indo-European languages.

As a joint thesis between linguistics and computer science, this thesis will continue the thesis work done in Fall 2017, which provides a thorough review of past computation models for language family homeland identification and concrete reasons for choosing the ASJP model over other models as the starting point. In Spring 2018, the work is mainly focused on improve the efficiency and accuracy of the modified model to exhibit the value of computational model applications in the field of linguistics.
