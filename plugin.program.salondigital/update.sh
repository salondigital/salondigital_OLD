#!/bin/bash
file=/home/htpc/.config/openbox/version.dat
minimumsize=70000
actualsize=$(wc -c <"$file")
if [ $actualsize -ge $minimumsize ]; then
    echo size is over $minimumsize bytes
		curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Comprobando el Sistema Operativo","message":"SalonDigital 1.2.1 64 bits"}}' http://localhost:8080/jsonrpc
		sleep 5
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando el sistema, no apague el equipo","message":"Por favor, espere a que el equipo se reinicie automaticamente"}}' http://localhost:8080/jsonrpc
sleep 2
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando el sistema, no apague el equipo","message":"Por favor, espere a que el equipo se reinicie automaticamente"}}' http://localhost:8080/jsonrpc
sleep 2
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando el sistema, no apague el equipo","message":"Por favor, espere a que el equipo se reinicie automaticamente"}}' http://localhost:8080/jsonrpc
sleep 2
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando el sistema, no apague el equipo","message":"Por favor, espere a que el equipo se reinicie automaticamente"}}' http://localhost:8080/jsonrpc
sleep 2
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando el sistema, no apague el equipo","message":"Por favor, espere a que el equipo se reinicie automaticamente"}}' http://localhost:8080/jsonrpc
mkdir /home/htpc/PROBANDOSCRIPT
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando","message":"1%"}}' http://localhost:8080/jsonrpc
mkdir /home/htpc/PROBANDOSCRIPT2
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando","message":"2%"}}' http://localhost:8080/jsonrpc
mkdir /home/htpc/PROBANDOSCRIPT3
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando","message":"3%"}}' http://localhost:8080/jsonrpc
mkdir /home/htpc/PROBANDOSCRIPT4
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando","message":"4%"}}' http://localhost:8080/jsonrpc
sleep 5
rm -rf /home/htpc/PROBANDOSCRIPT
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando","message":"5%"}}' http://localhost:8080/jsonrpc
rm -rf /home/htpc/PROBANDOSCRIPT2
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando","message":"6%"}}' http://localhost:8080/jsonrpc
rm -rf /home/htpc/PROBANDOSCRIPT3
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando","message":"7%"}}' http://localhost:8080/jsonrpc
rm -rf /home/htpc/PROBANDOSCRIPT4
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Actualizando","message":"8%"}}' http://localhost:8080/jsonrpc
sleep 1
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Reiniciando equipo","message":"Por favor, espere"}}' http://localhost:8080/jsonrpc
sleep 7
/home/htpc/Documentos/Apagar.sh
else
    echo size is under $minimumsize bytes
	curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":1,"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Comprobando el Sistema Operativo","message":"El S.O no es Salondigital, apagando..."}}' http://localhost:8080/jsonrpc
	sleep 4
	/home/htpc/Documentos/Apagar.sh
fi
