<template>
  <header class="border-b border-gray-200 bg-white sticky w-dvw flex justify-center">
    <div class="flex items-center justify-between p-4 max-w-3xl w-full">
      <h1 class="text-xl font-semibold text-gray-900">Chat IA</h1>
      <ModelSelector />
    </div>
  </header>
</template>

<script setup>
  import ModelSelector from './ModelSelector.vue'
</script>