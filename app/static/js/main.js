document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-form');
    const submitBtn = document.getElementById('submit-btn');
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');
    const errorText = document.getElementById('error-text');
    const resetBtn = document.getElementById('reset-btn');
    const messageInput = document.getElementById('message');
    const charCount = document.getElementById('char-count');
    
    const fields = {
        name: document.getElementById('name'),
        email: document.getElementById('email'),
        subject: document.getElementById('subject'),
        message: document.getElementById('message')
    };
    
    const errorElements = {
        name: document.getElementById('name-error'),
        email: document.getElementById('email-error'),
        subject: document.getElementById('subject-error'),
        message: document.getElementById('message-error')
    };
    
    // Character counter
    const MAX_MESSAGE_LENGTH = 2000;
    
    messageInput.addEventListener('input', () => {
        const length = messageInput.value.length;
        charCount.textContent = `${length} / ${MAX_MESSAGE_LENGTH}`;
        charCount.classList.remove('warning', 'limit');
        if (length >= MAX_MESSAGE_LENGTH) {
            charCount.classList.add('limit');
        } else if (length >= MAX_MESSAGE_LENGTH * 0.9) {
            charCount.classList.add('warning');
        }
    });
    
    // Real-time validation on blur
    Object.keys(fields).forEach(fieldName => {
        fields[fieldName].addEventListener('blur', () => validateField(fieldName));
        fields[fieldName].addEventListener('input', () => {
            if (errorElements[fieldName].classList.contains('visible')) {
                validateField(fieldName);
            }
        });
    });
    
    function validateField(fieldName) {
        const field = fields[fieldName];
        const errorEl = errorElements[fieldName];
        const value = field.value.trim();
        let error = '';
        
        if (!value) {
            error = `${capitalize(fieldName)} is required`;
        } else if (fieldName === 'name' && value.length > 100) {
            error = 'Name must be 100 characters or less';
        } else if (fieldName === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
            error = 'Please enter a valid email';
        } else if (fieldName === 'subject' && value.length > 200) {
            error = 'Subject must be 200 characters or less';
        } else if (fieldName === 'message' && value.length > 2000) {
            error = 'Message must be 2000 characters or less';
        }
        
        if (error) {
            showError(field, errorEl, error);
            return false;
        } else {
            clearError(field, errorEl);
            return true;
        }
    }
    
    function showError(field, errorEl, message) {
        field.classList.add('input-error');
        field.classList.remove('input-success');
        errorEl.textContent = message;
        errorEl.classList.add('visible');
    }
    
    function clearError(field, errorEl) {
        field.classList.remove('input-error');
        field.classList.add('input-success');
        errorEl.textContent = '';
        errorEl.classList.remove('visible');
    }
    
    function capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
    
    // Form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Validate all fields
        let isValid = true;
        Object.keys(fields).forEach(fieldName => {
            if (!validateField(fieldName)) {
                isValid = false;
            }
        });
        
        if (!isValid) return;
        
        // Show loading state
        setLoading(true);
        
        const formData = {
            name: fields.name.value.trim(),
            email: fields.email.value.trim(),
            subject: fields.subject.value.trim(),
            message: fields.message.value.trim()
        };
        
        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (response.ok && data.success) {
                showSuccess();
            } else if (response.status === 400 && data.errors) {
                handleValidationErrors(data.errors);
            } else {
                showErrorMessage(data.message || 'An error occurred. Please try again.');
            }
        } catch (error) {
            showErrorMessage('Network error. Please check your connection and try again.');
        } finally {
            setLoading(false);
        }
    });
    
    function setLoading(loading) {
        submitBtn.disabled = loading;
        submitBtn.classList.toggle('loading', loading);
        Object.values(fields).forEach(field => field.disabled = loading);
    }
    
    function handleValidationErrors(errors) {
        Object.keys(errors).forEach(fieldName => {
            if (errorElements[fieldName]) {
                showError(fields[fieldName], errorElements[fieldName], errors[fieldName]);
            }
        });
        // Focus first error field
        const firstErrorField = document.querySelector('.input-error');
        if (firstErrorField) {
            firstErrorField.focus();
            firstErrorField.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }
    
    function showSuccess() {
        form.hidden = true;
        successMessage.hidden = false;
        successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    
    function showErrorMessage(message) {
        errorText.textContent = message;
        errorMessage.hidden = false;
        form.hidden = true;
        errorMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            errorMessage.hidden = true;
            form.hidden = false;
        }, 5000);
    }
    
    // Reset form
    resetBtn.addEventListener('click', () => {
        form.reset();
        form.hidden = false;
        successMessage.hidden = true;
        charCount.textContent = '0 / 2000';
        charCount.classList.remove('warning', 'limit');
        
        // Clear all validation states
        Object.keys(fields).forEach(fieldName => {
            fields[fieldName].classList.remove('input-error', 'input-success');
            errorElements[fieldName].classList.remove('visible');
        });
        
        fields.name.focus();
    });
});
