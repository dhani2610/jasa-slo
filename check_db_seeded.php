<?php

require __DIR__ . '/vendor/autoload.php';
$app = require_once __DIR__ . '/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\Program;
use App\Models\Article;

echo "Database Programs: " . Program::count() . PHP_EOL;
foreach (Program::all() as $p) {
    echo "- [" . $p->slug . "] " . $p->title . PHP_EOL;
}

echo PHP_EOL . "Database Articles: " . Article::count() . PHP_EOL;
foreach (Article::all() as $a) {
    echo "- [" . $a->slug . "] " . $a->title . PHP_EOL;
}
