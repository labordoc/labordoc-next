
<div class="row">

  <div id="title">
    <span>
    {{ bfe_ilo_itemsymbol(bfo) }}
    </span>
    {{ bfe_ilo_title_with_link(bfo, highlight="no") }}
  </div>

 <div class="detailsBriefContent" style="margin-left: 5%";>

  {{ bfe_ilo_authors(bfo, prefix_en='<div id="authors"><div class="formatRecordLabel"> Author(s) </div>
					  		   <div class="positionDetailsBrief">',
					   	  prefix_es='<div id="authors"><div class="formatRecordLabel"> Autor(es) </div>
					  		   <div class="positionDetailsBrief">',
					      prefix_fr='<div id="authors"><div class="formatRecordLabel"> Auteur(s) </div>
					  		   <div class="positionDetailsBrief">',
						  suffix='</div></div>',
  				   		  limit="25", interactive="yes", print_affiliations="yes",
  				   		  affiliation_prefix="<small>(", affiliation_suffix=")</small>") }}

  {{ bfe_ilo_abstract(bfo, prefix_en='<div id="abstract"><div class="formatRecordLabel"> Abstract </div>
					  		   <div class="positionDetailsBrief">',
					   	 prefix_es='<div id="abstract"><div class="formatRecordLabel"> Resumen </div>
					  		   <div class="positionDetailsBrief">',
					     prefix_fr='<div id="abstract"><div class="formatRecordLabel"> Résumé </div>
					  		   <div class="positionDetailsBrief">',
						 suffix='</div></div>', limit="1") }}
  
  {{ bfe_ilo_date(bfo, prefix_en='<div id="date"><div class="formatRecordLabel"> Year </div>
					  		   <div class="positionDetailsBrief">',
					   prefix_es='<div id="date"><div class="formatRecordLabel"> Año </div>
					  		   <div class="positionDetailsBrief">',
					   prefix_fr='<div id="date"><div class="formatRecordLabel"> Année </div>
					  		   <div class="positionDetailsBrief">',
			  		   suffix='</div></div>') }}

  {{ bfe_ilo_links(bfo, prefix_en='<div id="links"><div class="formatRecordLabel"> Links </div>
					             <div class="positionDetailsBrief">',
					  prefix_es='<div id="links"><div class="formatRecordLabel"> Enlaces </div>
					             <div class="positionDetailsBrief">',
					  prefix_fr='<div id="links"><div class="formatRecordLabel"> Liens </div>
					             <div class="positionDetailsBrief">',
			          suffix='</div></div>',
			          separator='<br />', default='', show_icons='yes') }}

  <div id="snippets">
    {{ tfn_get_fulltext_snippets(record['recid'], request.args['p']) | wrap(prefix='<div class="formatRecordLabel"> Snippets </div>
                                                                   					<div class="positionDetailsBrief">', suffix='</div>') }}
  </div>

   
   {{ bfe_ilo_subjects(bfo, prefix_en='<div id="subjects"><div class="formatRecordLabel"> Subjects </div>
					  		   <div class="detailsSmallSize positionDetailsBrief">',
					   	 prefix_es='<div id="subjects"><div class="formatRecordLabel"> Temas </div>
					  		   <div class="detailsSmallSize positionDetailsBrief">',
					     prefix_fr='<div id="subjects"><div class="formatRecordLabel"> Sujets </div>
					  		   <div class="detailsSmallSize positionDetailsBrief">',
						 suffix='</div></div>') }}

  <div id="tags">
   {{ tfn_webtag_record_tags(record['recid'], current_user.get_id(), 'hb') }}
  </div>
</div>

</div !-- row --!>
