(function () {

'use strict';

angular.module('OpenSlidesApp.openslides_csv_export.site', ['OpenSlidesApp.openslides_csv_export'])

.config([
    'mainMenuProvider',
    'gettext',
    function (mainMenuProvider, gettext) {
        mainMenuProvider.register({
            'ui_sref': 'openslides_csv_export_overview',
            'img_class': 'download',
            'title': gettext('CSV Export'),
            'weight': 2000,
            'perm': 'agenda.can_manage',
        });
    }
])

.config([
    '$stateProvider',
    function ($stateProvider) {
        $stateProvider
            .state('openslides_csv_export_overview', {
                url: '/openslides_csv_export',
                templateUrl: 'static/templates/openslides_csv_export/overview.html',
            });
    }
]);

}());
