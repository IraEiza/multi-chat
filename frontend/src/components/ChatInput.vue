<template>
  <div class="fixed bottom-0 left-0 right-0 bg-white/90 backdrop-blur-sm border-t border-gray-200 px-4 py-3">
    <div class="max-w-3xl mx-auto">
      <form @submit.prevent="sendMessage" class="relative flex items-center">
      <textarea
        v-model="inputMessage"
        @keydown.enter.exact.prevent="sendMessage"
        placeholder="Escribe un mensaje..."
        class="w-full px-4 py-3 pr-12 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
        rows="1"
        :disabled="isLoading"
      />
      <button
        type="submit"
        :disabled="!inputMessage.trim() || isLoading"
        class="absolute right-2 bottom-2 p-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        @click="sendMessage"
      >
        <svg class="w-5 h-5 rotate-90" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
        </svg>
      </button>
    </form>
      <p class="text-xs text-gray-500 mt-2 text-center">
        Presiona Enter para enviar, Shift + Enter para nueva línea
      </p>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { storeToRefs } from 'pinia'
  import { useChatStore } from "../store/chat"

  const chat = useChatStore()
  const { addMessage, updateMessageContent } = chat
  const { messages, selectedModel } = storeToRefs(chat)
  
  const inputMessage = ref('')
  const isLoading = ref(false)

  const sendMessage = () => {
    const text = inputMessage.value.trim()
    if (!text || isLoading.value) return

    addMessage({
      id: crypto.randomUUID(),
      role: 'user',
      content: text
    })
    
    // TODO: Integrate with backend AI response
    const aiId = crypto.randomUUID()
    addMessage({
      id: aiId,
      role: 'ai',
      model: selectedModel.value.name,
      content: null
    })

    setTimeout(() => {
      const simulated = 'Hola! Soy tu asistente personal de IA. ¿En qué puedo ayudarte hoy?'
      updateMessageContent(aiId, simulated)
    }, 1500)

    inputMessage.value = ''
  }
</script>
  