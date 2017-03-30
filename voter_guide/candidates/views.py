# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Count, Sum, Q
from .models import Candidates


def districts(request, election_year, county):
    districts = Candidates.objects.filter(election_year=election_year, county=county).values('constituency', 'district')\
                                  .annotate(candidates=Count('id'))\
                                  .order_by('constituency')
    return render(request, 'candidates/districts.html', {'election_year': election_year, 'county': county, 'districts': districts})

def district(request, election_year, county, constituency):
    candidates = Candidates.objects.filter(election_year=election_year, county=county, constituency=constituency).order_by('-votes')\
                                   .annotate(
                                       balance=Sum('councilor__each_terms__politicalcontributions__balance'),
                                       in_total=Sum('councilor__each_terms__politicalcontributions__in_total'),
                                       out_total=Sum('councilor__each_terms__politicalcontributions__out_total')
                                   )
    return render(request, 'candidates/district.html', {'election_year': election_year, 'county': county, 'candidates': candidates})
