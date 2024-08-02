## Find all scan visits where LV score is > 1

```
SELECT ?patientID ?scanvisit ?LVqualityscore
# SELECT ?scanvisit ?LVqualityscore
WHERE {
  ?scanvisit rdf:type cmrqa:Imaging_Scan_Visit.
  ?scanvisit cmrqa:hasQualityData ?qualitydata.
  ?scanvisit cmrqa:participantName ?patientID.
  ?qualitydata cmrqa:hasLVQualityScore ?LVqualityscore
  FILTER(?LVqualityscore >1)
 
  

  # cmrqa:hasLVQualityScore > 1
}
LIMIT 10

```

## Give me the participant name for all the scan visits where LV score >1