{#-
## This file is part of Invenio.
## Copyright (C) 2012 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
-#}

{# add button to print output #}

<style>

.ibib-body {
 font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
 font-size: 14px;
 line-height: 20px;
}

</style>

<div class="button-print-ibib">

	<div id="print-button">
		 <button style="float:right;position:relative;font-size:16px;" onclick="printbib()">
		 <i class="fa fa-print"></i>
		 <span>Print</span>
		 </button>
	</div>
	<br />
    <br />
	<div id="records" class="ibib-body">
		{% for recid in recids %}
		  {{ format_record(recid, of).decode('utf-8') }}
		{% endfor %}
	</div>

</div>

{% block javascript %}
	<script>
	 function printbib()
	 {
	     if(!document.getElementsByClassName) {
	        document.getElementsByClassName = function (className) {
	        return document.querySelectorAll('.' + className)
	        }
	      }
	      var printEle = document.getElementsByClassName("button-print-ibib");
	      var printWin = window.open("");
	      printWin.document.write(printEle[0].innerHTML)
	      printWin.document.title = 'Records in Bibliographic format';
	      if (navigator.appName == 'Microsoft Internet Explorer') window.print();
	      else printWin.print();
	      printWin.close();
	 }
	</script>
{% endblock javascript %}
