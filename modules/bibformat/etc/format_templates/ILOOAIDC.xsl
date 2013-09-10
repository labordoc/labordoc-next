<?xml version="1.0" encoding="UTF-8"?>
<!-- $Id$

     This file is part of Invenio.
     Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010 CERN.

     Invenio is free software; you can redistribute it and/or
     modify it under the terms of the GNU General Public License as
     published by the Free Software Foundation; either version 2 of the
     License, or (at your option) any later version.

     Invenio is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
     General Public License for more details.  

     You should have received a copy of the GNU General Public License
     along with Invenio; if not, write to the Free Software Foundation, Inc.,
     59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
-->
<!--
<name>DC</name>
<description>XML Dublin Core</description>
-->


<!--
This stylesheet transforms a MARCXML input into an DC output.     
-->


<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:marc="http://www.loc.gov/MARC21/slim" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:dc="http://purl.org/dc/elements/1.1/" 
xmlns:fn="http://cdsweb.cern.ch/bibformat/fn"
exclude-result-prefixes="marc fn">
        <xsl:output method="xml"  indent="yes" encoding="UTF-8" omit-xml-declaration="yes"/>
        <xsl:template match="/">
		<xsl:if test="collection">
			<dc:collection xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd">
				<xsl:for-each select="collection">
					<xsl:for-each select="record">
						<dc:dc>
							<xsl:apply-templates select="."/>
						</dc:dc>
					</xsl:for-each>
				</xsl:for-each>
			</dc:collection>
		</xsl:if>
		<xsl:if test="record">
			<dc:dc xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd" xmlns:dc="http://purl.org/dc/elements/1.1/">
				<xsl:apply-templates/>
			</dc:dc>
		</xsl:if>
        </xsl:template>
        <xsl:template match="record">
	        <xsl:for-each select="datafield[@tag=245]">
			<dc:title>
                                <xsl:value-of select="subfield[@code='a']"/>
                                <xsl:if test="subfield[@code='b']">
                                     <xsl:text> </xsl:text>
                                     <xsl:value-of select="translate(subfield[@code='b'],'/','')"/>                                       
                                </xsl:if>
			</dc:title>
		</xsl:for-each>
	        <xsl:for-each select="datafield[@tag=100]|datafield[@tag=110]|datafield[@tag=111]|datafield[@tag=700]|datafield[@tag=710]|datafield[@tag=711]|datafield[@tag=720]">
			<dc:creator>
                                <xsl:value-of select="."/>
			</dc:creator>
		</xsl:for-each>


	        <xsl:for-each select="datafield[@tag=996]">
			<dc:type>
           			<xsl:choose>
	        			<xsl:when test="subfield[@code='a'] ='am'">text</xsl:when>
	        			<xsl:when test="subfield[@code='a'] ='as'">text</xsl:when>
	        			<xsl:when test="subfield[@code='a'] ='aa'">text</xsl:when>
	        			<xsl:when test="subfield[@code='a'] ='gm'">moving image</xsl:when>
	        			<xsl:when test="subfield[@code='a'] ='mm'">software, multimedia</xsl:when>
	        			<xsl:when test="subfield[@code='a'] ='cm'">notated music</xsl:when>
		                        <xsl:otherwise>text</xsl:otherwise>
        			</xsl:choose>
			</dc:type>
		</xsl:for-each>

	        <xsl:for-each select="datafield[@tag=992]">
			<dc:type>
                                <xsl:value-of select="subfield[@code='a']"/>
			</dc:type>
		</xsl:for-each>



	        <xsl:for-each select="datafield[@tag=655]">
           			<xsl:choose>
	        			<xsl:when test="subfield[@code='a'] ='ILO pub'"></xsl:when>
	        			<xsl:when test="subfield[@code='a'] ='pub OIT'"></xsl:when>
		                        <xsl:otherwise>
			                   <dc:type>
	                                     <xsl:value-of select="subfield[@code='a']"/>
			                   </dc:type>
                                        </xsl:otherwise>
        			</xsl:choose>
		</xsl:for-each>

		<xsl:for-each select="datafield[@tag=260]">
			<dc:publisher>
                                <xsl:value-of select="subfield[@code='b']"/>
                                <xsl:if test="subfield[@code='a']">
                                     <xsl:text> </xsl:text>
                                     <xsl:value-of select="translate(subfield[@code='a'],':','')"/>                                       
                                </xsl:if>
			</dc:publisher>
		</xsl:for-each>

	        <xsl:for-each select="datafield[@tag=997]">
			<dc:date>
                                <xsl:value-of select="subfield[@code='a']"/>
			</dc:date>
		</xsl:for-each>


	        <xsl:for-each select="datafield[@tag=998]">
			<dc:language>
                                <xsl:value-of select="subfield[@code='a']"/>
			</dc:language>
		</xsl:for-each>

	        <xsl:for-each select="datafield[@tag=520]">
			<dc:description>
                                <xsl:value-of select="subfield[@code='a']"/>
			</dc:description>
		</xsl:for-each>

	        <xsl:for-each select="datafield[@tag=505]">
			<dc:description>
                                <xsl:value-of select="subfield[@code='a']"/>
			</dc:description>
		</xsl:for-each>

	        <xsl:for-each select="datafield[@tag=650]">
			<dc:subject>
                                <xsl:value-of select="subfield[@code='a']"/>
			</dc:subject>
		</xsl:for-each>

	        <xsl:for-each select="controlfield[@tag=001]">
			<dc:identifier>
                                <xsl:text>recid: </xsl:text>
                                <xsl:value-of select="."/>
			</dc:identifier>
		</xsl:for-each>

	        <xsl:for-each select="datafield[@tag=020]">
			<dc:identifier>
                                <xsl:text>ISBN/ISSN: </xsl:text>
                                <xsl:value-of select="subfield[@code='a']"/>
			</dc:identifier>
		</xsl:for-each>

	        <xsl:for-each select="datafield[@tag=856 and @ind1=4]">
			<dc:identifier>
                                <xsl:value-of select="subfield[@code='u']"/>
			</dc:identifier>
		</xsl:for-each>

	        <xsl:for-each select="datafield[@tag=856 and @ind1=4]">
			<dc:identifier>
                                <xsl:value-of select="subfield[@code='u']"/>
			</dc:identifier>
		</xsl:for-each>
                <dc:source>
                    <xsl:value-of select="fn:eval_bibformat(controlfield[@tag=001],'&lt;BFE_SERVER_INFO var=&quot;recurl&quot; >')" />
                </dc:source>

        </xsl:template>
</xsl:stylesheet>
