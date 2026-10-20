<?php

require __DIR__ . '/vendor/autoload.php';
$app = require_once __DIR__ . '/bootstrap/app.php';

use App\Services\AhliK3UmumSchemeService;

$titles = AhliK3UmumSchemeService::get200ArticleTitles();
echo "Total titles: " . count($titles) . PHP_EOL;
echo "Title 1: " . $titles[0] . PHP_EOL;
echo "Title 2: " . $titles[1] . PHP_EOL;
echo "Title 3: " . $titles[2] . PHP_EOL;
