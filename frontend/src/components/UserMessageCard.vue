<template>
  <div 
  class="flex items-end gap-4 w-full mt-4"
  @mouseenter="startHover"
  @mouseleave="endHover"
  >
    <!-- Message column -->
    <div class="flex-1 min-w-0 flex flex-col items-end">
      <!-- Message bubble -->
      <div class="w-[90%] bg-blue-600 text-white p-4 rounded-xl rounded-br-none max-w-full">
        <!-- Editing state -->
        <div v-if="isEditing">
          <textarea
            v-model="editedText"
            @keydown.enter.exact.prevent="saveEdit"
            @keydown.esc="cancelEdit"
            class="w-full p-3 pr-24 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none bg-white text-gray-700"
            rows="3"
          />
          <div class="flex gap-2 mt-2">
            <button
              @click="saveEdit"
              class="px-3 py-1.5 bg-blue-800 text-white text-sm font-medium rounded-lg hover:bg-blue-700 transition-colors"
            >
              Guardar
            </button>
            <button
              @click="cancelEdit"
              class="px-3 py-1.5 bg-gray-200 text-gray-700 text-sm font-medium rounded-lg hover:bg-gray-300 transition-colors"
            >
              Cancelar
            </button>
          </div>
        </div>

        <!-- Read-only state -->
        <div
          v-else
          class="wrap-break-word leading-relaxed text-end"
        >
          {{ message }}
        </div>
      </div>

      <!-- Edit button -->
      <button
        @click="isEditing = true"
        class="mt-2 p-2 bg-white border border-gray-200 rounded-lg shadow-sm transition-opacity duration-200"
        :class="{
          'opacity-100 pointer-events-auto': showEditButton && !isEditing,
          'opacity-0 pointer-events-none': !showEditButton || isEditing
        }"
        title="Editar mensaje"
      >
        <svg
          class="w-4 h-4 text-gray-600"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
          />
        </svg>
      </button>
    </div>

    <!-- User icon -->
    <div class="shrink-0 w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center">
      <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
        <path
          fill-rule="evenodd"
          d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const { message } = defineProps({
  message: {
    type: String,
    required: true
  }
})

const isEditing = ref(false)
const editedText = ref(message)
const showEditButton = ref(false)
let hoverTimeout = null

function startHover() {
  hoverTimeout = setTimeout(() => {
    showEditButton.value = true
  }, 500)
}

function endHover() {
  clearTimeout(hoverTimeout)
  showEditButton.value = false
}

function saveEdit() {
  isEditing.value = false
  emit('update:message', editedText.value)
}

function cancelEdit() {
  isEditing.value = false
}

const emit = defineEmits(['update:message'])
</script>
