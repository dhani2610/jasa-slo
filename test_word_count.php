<?php

require __DIR__ . '/vendor/autoload.php';
$app = require_once __DIR__ . '/bootstrap/app.php';

use App\Services\AhliK3UmumSchemeService;

$art = AhliK3UmumSchemeService::generateDeepArticle('Training Ahli K3 Umum Resmi di Jawa Barat', 'Jawa Barat');
$wordCount = str_word_count(strip_tags($art['content']));

echo "Title: " . $art['title'] . PHP_EOL;
echo "Word count: " . $wordCount . PHP_EOL;
