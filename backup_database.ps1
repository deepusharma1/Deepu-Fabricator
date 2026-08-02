# Deepu Fabricator PostgreSQL Backup Script

$DATE = Get-Date -Format "yyyy-MM-dd_HH-mm"

$BACKUP_DIR = ".\backup\database"

$FILE = "$BACKUP_DIR\deepu_fabricator_$DATE.sql"


Write-Host "Starting Database Backup..."

docker exec deepu-fabricator-db `
pg_dump -U deepu_user deepu_fabricator `
> $FILE


if (Test-Path $FILE) {

    Write-Host "Backup Completed Successfully"
    Write-Host "File: $FILE"

}
else {

    Write-Host "Backup Failed"

}


# Keep last 30 days backup

Get-ChildItem $BACKUP_DIR -Filter "*.sql" |
Where-Object {
    $_.LastWriteTime -lt (Get-Date).AddDays(-30)
} |
Remove-Item -Force


Write-Host "Old backup cleanup completed"