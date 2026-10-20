<?php

require __DIR__ . '/vendor/autoload.php';
$app = require_once __DIR__ . '/bootstrap/app.php';

use App\Services\JasaSloSchemeService;

$programs = JasaSloSchemeService::getMasterPrograms();
echo "Total programs: " . count($programs) . PHP_EOL;
foreach ($programs as $i => $p) {
    echo ($i + 1) . ". [" . $p['slug'] . "] " . $p['title'] . PHP_EOL;
}

$titles = JasaSloSchemeService::get200ArticleTitles();
echo PHP_EOL . "Total titles: " . count($titles) . PHP_EOL;
echo "Title 1: " . $titles[0] . PHP_EOL;
echo "Title 2: " . $titles[1] . PHP_EOL;
echo "Title 200: " . $titles[199] . PHP_EOL;

$art = JasaSloSchemeService::generateDeepArticle('Training Jasa SLO: Panduan Lengkap Sertifikasi Laik Operasi Ketenagalistrikan di Jawa Barat', 'Jawa Barat');
$wc = str_word_count(strip_tags($art['content']));
echo PHP_EOL . "Article Word Count: " . $wc . " words." . PHP_EOL;
