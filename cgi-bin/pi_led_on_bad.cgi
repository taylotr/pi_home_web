#!/usr/bin/env python
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Bash as CGI"
echo "</title></head><body>"
echo "<h1>General system information for host $(hostname -s)</h1>"
echo ""
echo "<h1>Script Execution Output</h1>"
#echo "<pre> $(/usr/share/nginx/www/pi_led_on.py) </pre>"
echo "<pre> $out = system("/usr/share/nginx/www/pi_led_on.py") </pre>"
#echo "<pre> $out = system("ls -l") </pre>"
echo $out
echo "<center>Information generated on $(date)</center>"
echo "</body></html>"
