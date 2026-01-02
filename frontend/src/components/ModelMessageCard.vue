<template>
  <div class="flex items-start gap-4">
    <!-- AI Icon -->
    <div class="shrink-0 w-8 h-8 bg-gray-200 rounded-full flex items-center justify-center">
      <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
      </svg>
    </div>
    <!-- Message content -->
    <div class="flex-1">
      <div class="flex items-center gap-2 mb-1">
        <span class="text-sm font-medium text-gray-900">{{ model }}</span>
      </div>

      <div v-if="!content" class="flex gap-1">
        <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0ms"></span>
        <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 150ms"></span>
        <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 300ms"></span>
      </div>
      
      <div v-else class="flex gap-1">
        {{ content }}
      </div>
    </div>
  </div>
</template>

<script setup>
  const { content, model } = defineProps({
    content: {
      type: String,
      required: false,
      default: null
    },
    model: {
      type: String,
      required: true
    }
  })

  console.log(content)
</script>