
# $cmd = 'status'
# $cmd = 'pull'
# $cmd = 'add .'
$cmd = 'commit -am "New Commit"'
# $cmd = 'push'

$verz = $ph, $o

# ================ end Setting

$ti = (Get-Culture).TextInfo
$cmdgro = $ti.totitlecase($cmd)
# Exit

Write-Host -ForegroundColor White "**** Start Gitman"
# Write-Host "`\n"
function gi_do ($git_rep) {
    Set-Location $git_rep.FullName
    # Write-Host "`\n"
    Write-Host -ForegroundColor White "[**** Git $cmdgro" $git_rep.fullname
    invoke-expression( "git $cmd")
}

$gd = Get-ChildItem $hw -exclude '.*' -directory
# Write-Host('gd find',$gd)

foreach ($elem in $gd) {
    if ('.git' -in (Get-ChildItem -Path $elem).name) {
        # Write-Output verz $elem
        gi_do $elem
    }
}

foreach ($elem in $verz) {
    # Write-Output $elem
    gi_do (Get-Item $elem)
}

Write-Host "`\n"
Write-Host -ForegroundColor White "**** End Gitman"

