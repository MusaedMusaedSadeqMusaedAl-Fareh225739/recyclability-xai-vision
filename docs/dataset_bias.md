# Dataset Bias Analysis (IMsitu example)

After manually reviewing **503** IMsitu training images:

| Demographic | Images | Proportion |
|-------------|--------|------------|
| Identifiably Black individuals | **5** | **1 %** |
| All other subjects              | 498  | 99 % |

### Ramifications
* Under-representation can lead to **systematically lower recall** for scenes containing Black people.  
* Potential reinforcement of societal bias when the vision model is embedded in public recycling kiosks.  
* Ethical & reputational risk for WMCN if certain communities are disadvantaged.

### Harm scenario
> A smart-bin rejects items more often in neighbourhoods where label images show darker skin tones, triggering higher contamination fees for those residents.

### Mitigation roadmap
* Extend dataset with at least **500** new images focused on under-represented demographics.  
* Report group-specific precision/recall in every model card.  
* Adopt *Fairness Through Unawareness* as the baseline; test proxy variables.


