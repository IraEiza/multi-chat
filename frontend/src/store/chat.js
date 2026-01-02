import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useChatStore = defineStore('chat', () => {
  const messages = ref([])
  const selectedModel = ref({
      id: 'gpt-4',
      name: 'GPT-4',
      description: 'Modelo más avanzado para tareas complejas'
    })

  function addMessage(message) {
    messages.value.push(message)
  }

  function updateMessageContent(id, content) {
    const msg = messages.value.find(m => m.id === id)
    if (msg) msg.content = content
  }

  function setModel(model) {
    selectedModel.value = model
  }

  return {
    messages,
    selectedModel,
    addMessage,
    setModel,
    updateMessageContent
  }
})