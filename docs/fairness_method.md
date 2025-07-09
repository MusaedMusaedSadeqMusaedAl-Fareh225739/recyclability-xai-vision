# Fairness Method – “Fairness Through Unawareness”

**Definition**  
Train the classifier *without* including sensitive attributes (race, ethnicity) or their direct proxies.

**Why chosen**  
* Simple to implement; aligns with GDPR data-minimisation.  
* Prevents *direct* discrimination in the pixel → label mapping.  

**Limitations**  
* Does **not** remove proxy bias (background, skin tone).  
* Must be paired with post-hoc metrics: Demographic Parity / Equalised Odds.  

**Implementation in this project**  
* No face-detection, no manual tagging of race.  
* Group-wise F1 reported in `07_final_evaluation.ipynb`.  


