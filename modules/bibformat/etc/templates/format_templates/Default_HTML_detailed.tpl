
<script language="JavaScript" src="http://www.ilo.org/webcommon/s-includes/popups.js" type="text/javascript"></script>

<div class="row span14">
  <div id="detailedrecord" class="span11 pull-left">
 
    <div id="title">
      {{ bfe_ilo_title(bfo, prefix='<h3 class="articleTitle">', suffix='</h3>') }}
    </div>

    <div class="bfe-actions span3 pull-right">

     <div id="itemsymbol" class="detailsCover">
	   {{ bfe_ilo_itemsymbol_detailed_test(bfo) }}
	 </div>

     <div id="actions">
       {{ format_record(recid, 'HDACT', ln=g.ln) }}
     </div>

    </div !-- bfe-actions --! >

	<div class="detailedcontent span8">
	
	  <div id="conventionsdoctype">
		{{ bfe_ilo_conventions_doctype(bfo, prefix='<div class="formatRecordLabel"></div>') }} 
 	  </div>

	  <div id="conventions">
		{{ bfe_ilo_conventions(bfo, prefix='<div class="formatRecordLabel"> Document type </div>
								     <div class="positionDetails detailsConventions">',
							 		suffix='</div>') }} 
 	  </div>

	  <div id="authors">
		  {{ bfe_ilo_authors(bfo, prefix='<div class="formatRecordLabel"> Author(s) </div>
		  						   <div class="positionDetails">',
		                   		  suffix='</div>',
		  				   		  limit="25", interactive="yes", print_affiliations="yes", 
		  				   		  affiliation_prefix="<small>(", affiliation_suffix=")</small>") }}
	  </div>

	  <div id="year">
		  {{ bfe_ilo_date(bfo, prefix='<div class="formatRecordLabel"> Year </div>
							  		   <div class="positionDetails">',
 					  		   suffix='</div>') }}
 	  </div>

 	  <div id="publisherplace">
 	    {{ bfe_ilo_publisher_place(bfo, prefix='<div class="formatRecordLabel"> Published </div>
 	    							            <div class="positionDetails">', 
                                        suffix="</div>") }}	  						     						   
	  </div>

	  <div id="series">
	    {{ bfe_ilo_series(bfo, prefix='<div class="formatRecordLabel"> Series </div>
	    						       <div class="positionDetails detailsSmallSize">',
 							   suffix='</div>') }}
 	  </div>
 
	  <div id="imprint">
	    {{ bfe_ilo_imprint(bfo, prefix='<div class="formatRecordLabel"> In </div>
	    						        <div class="positionDetails detailsSmallSize">',
 						        suffix='</div>') }}
 	  </div>

	  <div id="meeting">
	    {{ bfe_ilo_meeting(bfo, prefix='<div class="formatRecordLabel"> Meeting </div>
	    						        <div class="positionDetails">',
 						        suffix='</div>') }}
 	  </div>
 
 	  <div id="reportnumbers">
	    {{ bfe_additional_report_numbers(bfo, prefix='<div class="formatRecordLabel"> Report number </div>
	    									          <div class="positionDetails">',
 						                      suffix='</div>',
 						                      separator=" ", link="no") }}
 	  </div>
 
	  <div id="conventionsreport">
	    {{ bfe_ilo_conventions_report(bfo, prefix='<div class="formatRecordLabel"> Report </div>
	    									       <div class="positionDetails">',
 									       suffix='</div>') }}
 	  </div>

	  <div id="pages">
	    {{ bfe_ilo_pages(bfo, prefix='<div class="formatRecordLabel"> Pages </div>
	    					          <div class="positionDetails">',
 					          suffix='</div>') }}
 	  </div>

 	  <div id="links">
	    {{ bfe_ilo_links(bfo, prefix='<div class="formatRecordLabel"> Links </div>
	    					          <div class="positionDetails detailsLinks">',
 					          suffix='</div>',
 					          separator='<br />', default='', show_icons='yes') }}
 	  </div>

 	  <div id="conventionslink">
	    {{ bfe_ilo_conventions_link(bfo, prefix='<span class="formatRecordLabel"> Links </span>
	    					                     <span class="positionDetails detailsConventions"><br /><b>',
 					                     suffix='</b></span>') }}
 	  </div>

 	  <div id="sfxlink">
	    {{ bfe_ilo_sfx_link(bfo, prefix='<div class="formatRecordLabel"> </div>
	    					             <div class="positionDetails"><br /><b>',
 					             suffix='</b></div>') }}
 	  </div>
 
 	  <div id="verticalspace" class="detailsEmptyRow" ></div>
 
 	  <div id="abstract">
	    {{ bfe_ilo_abstract(bfo, prefix='<div class="formatRecordLabel"> Abstract </div>
	    					             <div class="positionDetails">',
 					             suffix='</div>') }}
 	  </div>

 	  <div id="verticalspace" class="detailsEmptyRow" ></div>
 
 	  <div id="contents">
	    {{ bfe_ilo_contents(bfo, prefix='<div class="formatRecordLabel"> Contents </div>
	    					             <div class="detailsSmallSize positionDetails">',
 					   			 suffix='</div> ') }}
 	  </div>

 	  <div id="isbn">
	    {{ bfe_ilo_isbn(bfo, prefix='<div class="formatRecordLabel"> ISBN </div>
	    					         <div class="positionDetails detailsSmallSize">',
 					         suffix='</div>',
 					         separator='<br />', default='') }}
 	  </div>

 	  <div id="issn">
	    {{ bfe_issn(bfo, prefix='<div class="formatRecordLabel"> ISNN </div>
	    					     <div class="positionDetails detailsSmallSize">',
 					     suffix='</div>',
 					     default='') }}
 	  </div>

 	  <div id="otherversions">
	    {{ bfe_ilo_other_versions(bfo, prefix='<div class="formatRecordLabel"> Other versions </div>
	    					                   <div class="positionDetails detailsSmallSize">
	    					                   <ul class="OtherVersionsList"><li class="OtherVersionsList">
											   <i class="icon-caret-right"></i>&nbsp;&nbsp;&nbsp;',
					                   suffix='</li></ul></div>',
 					                   separator='</li><li class="OtherVersionsList"><i class="icon-caret-right"></i>&nbsp;&nbsp;&nbsp;',
 					                   default='') }}
 	  </div>

 	  <div id="verticalspace" class="detailsEmptyRow" ></div>

 	  <div id="subjects">
	    {{ bfe_ilo_subjects(bfo, keyword_prefix='<div class="formatRecordLabel"> Subjects </div>
	    					                     <div class="detailsSmallSize positionDetails">',
 					             keyword_suffix='</div>') }}
 	  </div>

	</div !-- detailedcontent --! >

   </div !-- detailedrecord --! >

</div !-- row --!>

