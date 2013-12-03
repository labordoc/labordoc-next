
{{ tfn_get_back_to_search_links(record['recid'])|wrap(prefix='<div class="pull-right linksbox">', suffix='</div>') }}

<div class="row">

  <div id="detailedrecord" class="span11 pull-left">
 
    <div id="title">
      {{ bfe_ilo_title(bfo, prefix='<h3 class="articleTitle">', suffix='</h3>') }}
    </div>

    <div class="bfe-actions span3 pull-right">

     <div id="itemsymbol" class="detailsCover">
	   {{ bfe_ilo_itemsymbol_detailed(bfo) }}
	 </div>

     <div id="actions">
       {{ format_record(recid, 'HDACT', ln=g.ln).decode('utf-8') }}
     </div>

    </div !-- bfe-actions --! >

	<div class="detailedcontent span8">
	
	{{ bfe_ilo_conventions_doctype(bfo) }} 

	{{ bfe_ilo_conventions(bfo, prefix='<div class="formatRecordLabel"> Document type </div>
							     <div class="positionDetails">',
						 		suffix='</div>') }} 

	{{ bfe_ilo_authors(bfo, prefix_en='<div id="authors"><div class="formatRecordLabel"> Author(s) </div>
					  		   <div class="positionDetails">',
					   	  	  prefix_es='<div id="authors"><div class="formatRecordLabel"> Autor(es) </div>
					  		   <div class="positionDetails">',
					      	  prefix_fr='<div id="authors"><div class="formatRecordLabel"> Auteur(s) </div>
					  		   <div class="positionDetails">',
						  	  suffix='</div></div>',
	  				   		  limit="25", interactive="yes", print_affiliations="yes", 
	  				   		  affiliation_prefix="<small>(", affiliation_suffix=")</small>") }}

    {{ bfe_ilo_date(bfo, prefix_en='<div id="date"><div class="formatRecordLabel"> Year </div>
					  		     <div class="positionDetails">',
					     prefix_es='<div id="date"><div class="formatRecordLabel"> Año </div>
					  		     <div class="positionDetails">',
					     prefix_fr='<div id="date"><div class="formatRecordLabel"> Année </div>
					  		     <div class="positionDetails">',
			  		     suffix='</div></div>') }}

    {{ bfe_ilo_publisher_place(bfo, prefix_en='<div id="place"><div class="formatRecordLabel"> Published </div>
    							            <div class="positionDetails">',
									prefix_es='<div id="place"><div class="formatRecordLabel"> Publicado </div>
    							            <div class="positionDetails">',
									prefix_fr='<div id="place"><div class="formatRecordLabel"> Publié </div>
    							            <div class="positionDetails">',     							                							            
                                    suffix="</div></div>") }}	  						     						   

    {{ bfe_ilo_series(bfo, prefix='<div class="formatRecordLabel"> Series </div>
    						       <div class="positionDetails">',
						   suffix='</div>') }}
 
    {{ bfe_ilo_imprint(bfo, prefix_en='<div id="imprint"><div class="formatRecordLabel"> In </div>
										<div class="positionDetails detailsSmallSize">',
							prefix_es='<div id="imprint"><div class="formatRecordLabel"> En </div>
										<div class="positionDetails detailsSmallSize">',
							prefix_fr='<div id="imprint"><div class="formatRecordLabel"> Dans </div>
										<div class="positionDetails detailsSmallSize">',
							suffix='</div></div>') }}

    {{ bfe_ilo_meeting(bfo, prefix='<div class="formatRecordLabel"> Meeting </div>
    						        <div class="positionDetails">',
					        suffix='</div>') }}
 
    {{ bfe_additional_report_numbers(bfo, prefix='<div class="formatRecordLabel"> Report number </div>
    									          <div class="positionDetails">',
					                      suffix='</div>',
					                      separator=" ", link="no") }}
 
    {{ bfe_ilo_conventions_report(bfo, prefix='<div class="formatRecordLabel"> Report </div>
    									       <div class="positionDetails">',
								       suffix='</div>') }}

    {{ bfe_ilo_pages(bfo, prefix_en='<div id="pages"><div class="formatRecordLabel"> Pages </div>
    					          <div class="positionDetails">',
						  prefix_es='<div id="pages"><div class="formatRecordLabel"> Páginas </div>
    					          <div class="positionDetails">',
						  prefix_fr='<div id="pages"><div class="formatRecordLabel"> Pages </div>
    					          <div class="positionDetails">', 					       
				          suffix='</div></div>') }}

    {{ bfe_ilo_links(bfo, prefix_en='<div id="links"><div class="formatRecordLabel"> Links </div>
					             <div class="positionDetails">',
						  prefix_es='<div id="links"><div class="formatRecordLabel"> Enlaces </div>
						             <div class="positionDetails">',
						  prefix_fr='<div id="links"><div class="formatRecordLabel"> Liens </div>
						             <div class="positionDetails">',
				          suffix='</div></div>',
				          separator='<br />', default='', show_icons='yes') }}

    {{ bfe_ilo_conventions_link(bfo, prefix='<div class="formatRecordLabel"> </div>
											<div class="positionDetails"><br /><b>',
									suffix='</b></div>') }}

	{{ bfe_ilo_sfx_link(bfo, prefix='<div class="formatRecordLabel"> </div>
	    					         <div class="positionDetails"><br /><b>',
 					         suffix='</b></div>') }}
  
    {{ bfe_ilo_abstract(bfo, prefix_en='<div id="abstract"><div class="formatRecordLabel"> Abstract </div>
						  		   <div class="positionDetails">',
						   	 prefix_es='<div id="abstract"><div class="formatRecordLabel"> Resumen </div>
						  		   <div class="positionDetails">',
						     prefix_fr='<div id="abstract"><div class="formatRecordLabel"> Résumé </div>
						  		   <div class="positionDetails">',
							 suffix='</div></div>') }}
 
  	<div id="verticalspace" class="detailsEmptyRow" ></div>
 
    {{ bfe_ilo_contents(bfo, prefix_en='<div id="contents"><div class="formatRecordLabel"> Contents </div>
    					             <div class="positionDetails">',
    					     prefix_es='<div id="contents"><div class="formatRecordLabel"> Contenidos </div>
    					             <div class="positionDetails">',
     					     prefix_fr='<div id="contents"><div class="formatRecordLabel"> Contenu </div>
    					             <div class="positionDetails">',     					      
				   			 suffix='</div></div>') }}

    {{ bfe_ilo_isbn(bfo, prefix='<div class="formatRecordLabel"> ISBN </div>
    					         <div class="positionDetails detailsSmallSize">',
				         suffix='</div>',
				         separator='<br />', default='') }}

    {{ bfe_issn(bfo, prefix='<div class="formatRecordLabel"> ISNN </div>
    					     <div class="positionDetails detailsSmallSize">',
				     suffix='</div>',
				     default='') }}

    {{ bfe_ilo_other_versions(bfo, prefix_en='<div id="other_versions"><div class="formatRecordLabel"> Other versions </div>
    					                   <div class="positionDetails detailsSmallSize">
    					                   <ul class="OtherVersionsList"><li class="OtherVersionsList">
										   <i class="icon-caret-right"></i>&nbsp;&nbsp;&nbsp;',
								   prefix_es='<div id="other_versions"><div class="formatRecordLabel"> Otras versiones </div>
    					                   <div class="positionDetails detailsSmallSize">
    					                   <ul class="OtherVersionsList"><li class="OtherVersionsList">
										   <i class="icon-caret-right"></i>&nbsp;&nbsp;&nbsp;',
								   prefix_fr='<div id="other_versions"><div class="formatRecordLabel"> Autre versions </div>
    					                   <div class="positionDetails detailsSmallSize">
    					                   <ul class="OtherVersionsList"><li class="OtherVersionsList">
										   <i class="icon-caret-right"></i>&nbsp;&nbsp;&nbsp;',
				                   suffix='</li></ul></div></div>',
				                   separator='</li><li class="OtherVersionsList"><i class="icon-caret-right"></i>&nbsp;&nbsp;&nbsp;',
				                   default='') }}

 	<div id="verticalspace" class="detailsEmptyRow" ></div>

    {{ bfe_ilo_subjects(bfo, prefix_en='<div id="subjects"><div class="formatRecordLabel"> Subjects </div>
					  		   <div class="detailsSmallSize positionDetails">',
						   	 prefix_es='<div id="subjects"><div class="formatRecordLabel"> Temas </div>
						  		   <div class="detailsSmallSize positionDetails">',
						     prefix_fr='<div id="subjects"><div class="formatRecordLabel"> Sujets </div>
						  		   <div class="detailsSmallSize positionDetails">',
							 suffix='</div></div>') }}

   <div id="verticalspace" class="detailsEmptyRow" ></div>

	{{ tfn_webtag_record_tags(record['recid'], current_user.get_id(), 'hd') }}

  </div !-- detailedcontent --! >

  </div !-- detailedrecord --! >

</div !-- row --!>

