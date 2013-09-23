<div class="row">

  <div id="title">
    <span>
    {{ bfe_ilo_itemsymbol(bfo) }}
    </span>
    {{ bfe_ilo_title_with_link(bfo, highlight="no") }}
  </div>

 <div class="detailsBriefContent span10" style="margin-left: 5%";>
  <div id="authors">
	  {{ bfe_ilo_authors(bfo, prefix='<div class="formatRecordLabel"> Author(s) </div>
	  						   <div class="positionDetailsBrief">',
	                   		  suffix='</div>',
	  				   		  limit="25", interactive="yes", print_affiliations="yes",
	  				   		  affiliation_prefix="<small>(", affiliation_suffix=")</small>") }}
  </div>

  <div id="abstract">
    {{ bfe_ilo_abstract(bfo, prefix='<div class="formatRecordLabel"> Abstract </div>
    					             <div class="positionDetailsBrief">',
				             suffix='</div>', limit="1") }}
  </div>
  <div id="year">
	  {{ bfe_ilo_date(bfo, prefix='<div class="formatRecordLabel"> Year </div>
						  		   <div class="positionDetailsBrief">',
				  		   suffix='</div>') }}
  </div>
  <div id="links">
    {{ bfe_ilo_links(bfo, prefix='<div class="formatRecordLabel"> Links </div>
    					          <div class="positionDetailsBrief detailsLinks">',
				          suffix='</div>',
				          separator='<br />', default='', show_icons='yes') }}
  </div>
  <div id="subjects">
    {{ bfe_ilo_subjects(bfo, keyword_prefix='<div class="formatRecordLabel"> Subjects </div>
    					                     <div class="detailsSmallSize positionDetailsBrief">',
				             keyword_suffix='</div>') }}
  </div>
</div>

</div !-- row --!>
