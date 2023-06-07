
import-module ActiveDirectory
$groupName = $env:GROUP_NAME
$group = Get-ADGroup -Filter {Name -eq $groupName} -Properties Name

if ($group) {
    Write-Host "Group $groupName exists in Active Directory."
} else {
    Write-Host "Group $groupName does not exist in Active Directory."
}

