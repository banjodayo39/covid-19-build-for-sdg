from django.db import models

class Estimator(models.Model):
    data = models.models.models.OneToOneField(Data, on_delete=models.CASCADE)
    impact = models.models.models.OneToOneField(Impact, on_delete=models.CASCADE)
    severeImpact = models.models.models.OneToOneField(SevereImpact, on_delete=models.CASCADE)

    def __str__(self):
        return '({0}, {1})'.format(self.data, self.impact)

class Data(models.Model):
    region = models.OneToOneField(Region, on_delete=models.CASCADE)
    periodType = models.CharField(max_length = 10)
    timeToElapse = models.IntegerField(max_length= 10)
    reportedCases = models.IntegerField(max_length= 10)
    population = models.IntegerField(max_length= 10)
    totalHospitalBeds = models.IntegerField(max_length= 10)
 
class Region(models.Model):
    name = models.CharField(max_length = 10)
    avgAge = models.IntegerField(max_length= 10)
    avgDailyIncomeInUSD = models.IntegerField(max_length= 10)
    avgDailyIncomePopulation = models.IntegerField(max_length= 10)

class Impact(models.Model):
     impact_currentlyInfected = models.IntegerField(max_length= 10)
     impact_infectionsByRequestedTime = models.IntegerField(max_length= 10)
     impact_severeCasesByRequestedTime = models.FloatField(max_length = 10)
     impact_hospitalBedsByRequestedTime = models.FloatField(max_length = 10) 
     impact_casesForICUByRequestedTime = models.FloatField(max_length = 10)
     impact_casesForVentilatorsByRequestedTime = models.FloatField(max_length = 10)
     impact_dollarsInFlight = models.FloatField(max_length = 10)

class SevereImpact(models.Model):   
     severeImpact_currentlyInfected = models.IntegerField(max_length= 10)
     severeImpact_infectionsByRequestedTime = models.IntegerField(max_length= 10)
     severeImpact_severeCasesByRequestedTime = models.FloatField(max_length = 10)
     severeImpact_hospitalBedsByRequestedTime = models.FloatField(max_length = 10) 
     severeImpact_casesForICUByRequestedTime = models.FloatField(max_length = 10)
     severeImpact_casesForVentilatorsByRequestedTime = models.FloatField(max_length = 10)
     severeImpact_dollarsInFlight = models.FloatField(max_length = 10)
     
