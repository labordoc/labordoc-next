<div class="row">

  <div>
    <div id="symbol" class="customspan1" style="text-align:right;">
	  {{ bfe_ilo_itemsymbol(bfo) }}
    </div>

	<div class="span6">

      <div id="title">
	    {{ bfe_ilo_title_with_link(bfo, highlight="no") }}
      </div>

    <div class="detailsBriefContent">
	
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
	
	  {{ bfe_ilo_links(bfo, prefix_en='<div id="links"><div class="formatRecordLabel"> Text </div>
	                                                     <div class="positionDetailsBrief">',
	                                          prefix_es='<div id="links"><div class="formatRecordLabel"> Texto </div>
	                                                     <div class="positionDetailsBrief">',
	                                          prefix_fr='<div id="links"><div class="formatRecordLabel"> Texte </div>
	                                                     <div class="positionDetailsBrief">',
	                                  suffix='</div></div>',
	                                  separator='<br />', default='', show_icons='yes') }}
	
	   
	   {{ bfe_ilo_subjects(bfo, prefix_en='<div id="subjects"><div class="formatRecordLabel"> Subjects </div>
	                                                             <div class="detailsSmallSize positionDetailsBrief">',
	                                                    prefix_es='<div id="subjects"><div class="formatRecordLabel"> Temas </div>
	                                                             <div class="detailsSmallSize positionDetailsBrief">',
	                                             prefix_fr='<div id="subjects"><div class="formatRecordLabel"> Sujets </div>
	                                                             <div class="detailsSmallSize positionDetailsBrief">',
	                                                 suffix='</div></div>') }}

	</div>

  </div>
 </div>
</div !-- row --!>
