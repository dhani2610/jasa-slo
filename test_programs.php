<?php

require __DIR__ . '/vendor/autoload.php';
$app = require_once __DIR__ . '/bootstrap/app.php';

use App\Services\AhliK3UmumSchemeService;

$programs = AhliK3UmumSchemeService::getMasterPrograms();
echo "Total programs: " . count($programs) . PHP_EOL;
foreach ($programs as $i => $p) {
    echo ($i + 1) . ". [" . $p['slug'] . "] " . $p['title'] . PHP_EOL;
}
