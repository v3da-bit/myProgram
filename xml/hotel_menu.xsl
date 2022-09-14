<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<body style="background-image:url('Taj-Mahal-Palace-Historic-Hotel-Mumbai-scaled.jpg'); background-repeat: no-repeat; background-size: 100%; image-resolution: 300dpi;">
<h1 align="center" style="color:red; font-size: 50;"><u><i>*Taj Group of Hotels*</i></u></h1>
<table style="width:98.4%; background-color: goldenrod; margin-left:6px; margin-right:10px; ">
<th style="font-size: 40; color:green">---MENU---</th>
</table>
<table border="0" align ="left" cellpadding="24" style="background-color: goldenrod; margin-left:6px">
	
    <tr style="font-size: 30; color:blue">
	<th>Starters</th>
	</tr>
    <tr style="font-size: 20; ">
        <th>Food Name</th>
        <th>price</th>
        </tr>
        
    <xsl:for-each select="food/starter">
    <tr>
    <td><xsl:value-of select="name"/></td>
	<td><xsl:value-of select="price"/></td>
	</tr>
    </xsl:for-each>
</table>
<table border="0" align ="left" cellpadding="24" style="background-color: goldenrod;">
 <tr style="font-size: 30;color:blue">
	<th>Paneer Ka Khazana</th>
	

    </tr>
    <tr style="font-size: 20;">
        <th>Food Name</th>
        <th>price</th>
        </tr>
    
	<xsl:for-each select="food/paneer">
        <tr>
        <td><xsl:value-of select="name1"/></td>
        <td><xsl:value-of select="price1"/></td>
        </tr>
        </xsl:for-each>
</table>
<table border="0" align ="left" cellpadding="24" style="background-color: goldenrod;">
<tr style="font-size: 30;color:blue">
	<th>Veg Sabji</th>
	

    </tr>
    <tr style="font-size: 20;">
        <th>Food Name</th>
        <th>price</th>
        </tr>
    
	<xsl:for-each select="food/veg">
        <tr>
        <td><xsl:value-of select="name2"/></td>
        <td><xsl:value-of select="price2"/></td>
        </tr>
        </xsl:for-each>
</table>
<table border="0" align ="left" cellpadding="24" style="background-color: goldenrod;">
 <tr style="font-size: 30;color:blue">
	<th>Fast Food</th>
	

    </tr>
    <tr style="font-size: 20;">
        <th>Food Name</th>
        <th>price</th>
        </tr>
    
	<xsl:for-each select="food/fast">
        <tr>
        <td><xsl:value-of select="name4"/></td>
        <td><xsl:value-of select="price4"/></td>
        </tr>
        </xsl:for-each>
</table>

<table border="0" align ="left" cellpadding="24" style="background-color: goldenrod;">
<tr style="font-size: 30;color:blue">
	<th>Sweet House</th>
	

    </tr>
    <tr style="font-size: 20;">
        <th>Food Name</th>
        <th>price</th>
        </tr>
    
	<xsl:for-each select="food/desert">
        <tr>
        <td><xsl:value-of select="name3"/></td>
        <td><xsl:value-of select="price3"/></td>
        </tr>
        </xsl:for-each>
</table>

</body>
</html>
</xsl:template>
</xsl:stylesheet>