# Defininig variables for "About Me"
$Name = "Saleban"
$Location = "Kansas City, Missouri"
$CareerGoal = "Entry-Level Security Consultant"
$Skills = @("Microsoft Intune Admin Center", "Active Directory", "Jira Ticketing System", "Data Privilege Management", "Proofpoint", "Exchange Admin Center")
$FunFact = "I build and sell gaming PCs to students aged 18-22."

Write-Output "About Me Script"
Write-Output "================"
Write-Output "Name: $Name"
Write-Output "Location: $Location"
Write-Output "Career Goal: $CareerGoal"
Write-Output "Skills:"
$Skills | ForEach-Object { Write-Output " - $_" }
Write-Output "Fun Fact: $FunFact"
Write-Output ""

$DirectoryPath = "$env:USERPROFILE\Documents\AboutMe_$Name"
if (-Not (Test-Path $DirectoryPath)) {
    New-Item -ItemType Directory -Path $DirectoryPath | Out-Null
    Write-Output "Created a folder at $DirectoryPath"
} else {
    Write-Output "Folder already exists at $DirectoryPath"
}

Write-Output ""
Write-Output "Let's interact! Please enter your favorite programming language:"
$FavoriteLanguage = Read-Host "Enter here"

Write-Output "Thank you! You entered: $FavoriteLanguage"


$OutputFile = "$DirectoryPath\AboutMe_Output.txt"
$OutputContent = @"
Name: $Name
Location: $Location
Career Goal: $CareerGoal
Skills: $(($Skills -join ", "))
Fun Fact: $FunFact
Favorite Programming Language: $FavoriteLanguage
"@
$OutputContent | Out-File -FilePath $OutputFile -Encoding UTF8
Write-Output "Your details have been written to $OutputFile"


Write-Output ""
Write-Output "Script executed successfully. Check your folder for the output file!"


