import json

def estimator(data):

  time = 0
  infection_time = 0
  impact_dollarsInFlight = 0
  severeImpact_dollarsInFlight = 0

  if data['periodType'] == "days":
    time = data['timeToElapse']
    infection_time = (int)(time/3)

  elif data['periodType'] == "weeks":
    time = data['timeToElapse'] * 7
    infection_time = (int)(time/3)
  
  elif data['periodType'] == "months":
    time = data['timeToElapse'] * 7
    infection_time = (int)(time/3)
    
  # Challenge 1
  impact_currentlyInfected = data['reportedCase'] * 10
  severeImpact_currentlyInfected = data['reportedCases'] * 50
  impact_infectionsByRequestedTime = impact_currentlyInfected * pow(2, infection_time)
  severeImpact_infectionsByRequestedTime = severeImpact_currentlyInfected * pow(2, infection_time)

  # Challenge 2
  impact_severeCasesByRequestedTime = impact_infectionsByRequestedTime * 0.15
  severeImpact_severeCasesByRequestedTime = severeImpact_infectionsByRequestedTime * 0.15
  impact_hospitalBedsByRequestedTime = (data['totalHospitalBeds'] * 0.35) - impact_severeCasesByRequestedTime
  severeImpact_hospitalBedsByRequestedTime = (data['totalHospitalBeds'] * 0.35) - severeImpact_severeCasesByRequestedTime
  
  #Challenge 3
  impact_casesForICUByRequestedTime = impact_infectionsByRequestedTime * 0.05 
  severeImpact_casesForICUByRequestedTime = 0.05 * severeImpact_infectionsByRequestedTime * 0.05
  impact_casesForVentilatorsByRequestedTime = impact_infectionsByRequestedTime * 0.02
  severeImpact_casesForVentilatorsByRequestedTime = severeImpact_infectionsByRequestedTime * 0.02

  
  impact_dollarsInFlight = (
      data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD:'] * impact_infectionsByRequestedTime
    )/ time

  severeImpact_dollarsInFlight =  (
      data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD:'] * severeImpact_infectionsByRequestedTime
    )/ time

 
  output = {
    "data" : data,
    "impact" : {
      "impact_currentlyInfected" : impact_currentlyInfected,
      "impact_infectionsByRequestedTime" : impact_infectionsByRequestedTime,
      "impact_severeCasesByRequestedTime" : impact_severeCasesByRequestedTime,
      "impact_hospitalBedsByRequestedTime" : impact_hospitalBedsByRequestedTime,
      "impact_casesForICUByRequestedTime" : impact_casesForICUByRequestedTime,
      "impact_casesForVentilatorsByRequestedTime" : impact_casesForVentilatorsByRequestedTime,
      "impact_dollarsInFlight" : impact_dollarsInFlight
 },
    "severeImpact": {
      "severeImpact_currentlyInfected" : severeImpact_currentlyInfected,
      "severeImpact_infectionsByRequestedTime" : severeImpact_infectionsByRequestedTime,
      "severeImpact_severeCasesByRequestedTime" : severeImpact_severeCasesByRequestedTime,
      "severeImpact_hospitalBedsByRequestedTime" : severeImpact_hospitalBedsByRequestedTime,
      "severeImpact_casesForICUByRequestedTime" : severeImpact_casesForICUByRequestedTime,
      "severeImpact_casesForVentilatorsByRequestedTime" : severeImpact_casesForVentilatorsByRequestedTime,
      "severeImpact_dollarsInFlight" : severeImpact_dollarsInFlight
    }
  }

  json_output = json.dumps(output)
  return json_output