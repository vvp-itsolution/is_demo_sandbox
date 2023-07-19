ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
        center: [59.94, 30.39],
        zoom: 10
    }, {
        searchControlProvider: 'yandex#search'
    });

    myMap.geoObjects
        .add(new ymaps.Placemark([55.684758, 37.738521], {
            balloonContent: 'цвет <strong>воды пляжа бонди</strong>'
        }, {
            preset: 'islands#icon',
            iconColor: '#0095b6'
        }));

    BX24.callMethod('crm.address.list', {select: ['ANCHOR_ID', 'ADDRESS_1', 'CITY']}, function (res) {
        let address = res.answer.result
        console.log(address)

        BX24.callMethod('crm.company.list', {select: ['ID', 'TITLE']}, function (res) {
            let Company = res.answer.result
            console.log(Company)

            Company.forEach(comp => {
                address.forEach(addr => {
                    if (comp['ID'] === addr['ANCHOR_ID']) {
                        ymaps.geocode(`${addr['CITY']}, ${addr['ADDRESS_1']}`, {}).then(function (res) {
                            var firstGeoObject = res.geoObjects.get(0),
                                coords = firstGeoObject.geometry.getCoordinates();
                            myMap.geoObjects
                                .add(new ymaps.Placemark(coords, {
                                    balloonContent: `<strong>${comp['TITLE']}</strong>, ${addr['ADDRESS_1']}`
                                }, {
                                    preset: 'islands#icon',
                                    iconColor: '#0095b6'
                                }));
                        })
                    }
                })
            })
        })
    })
}
