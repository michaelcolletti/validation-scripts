


Import-Module ActiveDirectory

# Prompt user for group name
$groupName = Read-Host "Enter group name"


# Parameterize this

# Check if group exists in Active Directory
if (Get-ADGroup -Filter {Name -eq $groupName}) {
    Write-Host "Group $groupName exists in Active Directory"
} else {
    Write-Host "Group $groupName does not exist in Active Directory"
}




