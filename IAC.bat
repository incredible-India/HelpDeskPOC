@echo off
:: Echo green text using PowerShell
powershell -Command "Write-Host 'IAC Building Project started' -ForegroundColor Green"

::Fisrt step start
powershell -Command "Write-Host 'AZ Login"
az login
powershell -Command "Write-Host 'AZ Login completed' -ForegroundColor Green"
::First step done
:: Second Step start
powershell -Command "Write-Host 'AZ Cred'"
az acr login -n incadea --subscription 637dabed-efa5-488a-8224-640a38eff47e
powershell -Command "Write-Host 'AZ Cred completed' -ForegroundColor Green"
:: Second step done
:: Third Step start
powershell -Command "Write-Host 'Pull Docker image'"
docker compose -f docker-compose.yaml pull
powershell -Command "Write-Host 'Pull Docker image completed' -ForegroundColor Green"
:: Third step done
:: Fourth Step start
powershell -Command "Write-Host 'neccessary tools and services'"
docker compose -f docker-compose.yaml up -d
powershell -Command "Write-Host 'neccessary tools and services completed' -ForegroundColor Green"
:: Fourth step done
:: Fifth Step start
powershell -Command "Write-Host 'Load further microservices'"
docker compose -f .\microservices\docker-compose-digital365-microservices.yaml up -d
powershell -Command "Write-Host 'Docker build completed' -ForegroundColor Green"
:: Fifth step done
:: Sixth Step start
powershell -Command "Write-Host 'Start Blazor App'"
docker compose -f .\microservices\docker-compose-blazor-server.yaml up -d
powershell -Command "Write-Host 'Start Blazor App completed' -ForegroundColor Green"
:: Sixth step done
:: Seventh Step start
powershell -Command "Write-Host 'Start Aftersales Workplace'"
docker compose -f .\microservices\docker-compose-aftersalesworkplace.yaml up -d
powershell -Command "Write-Host 'Start Aftersales Workplace completed' -ForegroundColor Green"
:: Seventh step done
:: Eighth Step start
powershell -Command "Write-Host 'Start AAdmin Portal'"
docker compose -f .\microservices\docker-compose-adminportal.yaml up -d
powershell -Command "Write-Host 'Start AAdmin Portal completed' -ForegroundColor Green"
:: Eighth step done

powershell -Command "Write-Host 'IAC Building Project completed' -ForegroundColor Green"
powershell -Command "Write-Host 'If you are using first time u need to execute the powershell script presented in Docker compose-> Certs folder' -ForegroundColor yellow"
powershell -Command "Write-Host 'You can close thisterminal now' -ForegroundColor Green"

pause
