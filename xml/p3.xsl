<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
version="1.0">
<xsl:template match="/">
<html>
<body>
<h1 align="center">Students</h1>
<table border="2" align="center">
<tr text-align="center">
<th>name</th>
<th>Enrollement Number</th>
<th>Email</th>
<th>Mobile Number</th>
<th>Address</th>
<th>College</th>
<th>Branch</th>
</tr>
<xsl:for-each select="class/student">
<tr text-align="center">
<td>
<xsl:value-of select="name"/>
</td>
<td>
<xsl:value-of select="enrollnment"/>
</td>
<td>
<xsl:value-of select="email"/>
</td>
<td>
<xsl:value-of select="mobile"/>
</td>
<td>
<xsl:value-of select="address"/>
</td>
<td>
<xsl:value-of select="college"/>
</td>
<td>
<xsl:value-of select="branch"/>
</td>
</tr>
</xsl:for-each>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>