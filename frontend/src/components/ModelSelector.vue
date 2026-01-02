<template>
  <div class="relative inline-block">
    <button
      @click="showModelSelector = !showModelSelector"
      class="flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-700 bg-gray-50 border border-gray-200 rounded-lg hover:bg-gray-100 transition-colors"
    >
      {{ selectedModel.name}}
      <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>

    <!-- Dropdown -->
    <Dropdown
      v-if="showModelSelector"
      :items="models"
      :selectedItem="selectedModel"
      @select="onSelect"
    />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { storeToRefs } from 'pinia'
  import { useChatStore } from "../store/chat"
  import Dropdown from './Dropdown.vue'

  const { selectedModel } = storeToRefs(useChatStore())

  // Models available
  const models = ref([
    {
      id: 'gpt-4',
      name: 'GPT-4',
      description: 'Modelo más avanzado para tareas complejas'
    },
    {
      id: 'gpt-3.5',
      name: 'GPT-3.5 Turbo',
      description: 'Rápido y eficiente para tareas generales'
    },
    {
      id: 'claude',
      name: 'Claude 3',
      description: 'Excelente para análisis y razonamiento'
    },
    {
      id: 'gemini',
      name: 'Gemini Pro',
      description: 'Modelo multimodal de Google'
    }
  ])

  const showModelSelector = ref(false)

  function onSelect(item) {
    selectedModel.value = item
    showModelSelector.value = false
  }
</script>
