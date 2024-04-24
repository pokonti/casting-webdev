import { Component } from '@angular/core';
import { FooterComponent } from "../footer/footer.component";
import { FormsModule } from '@angular/forms';
@Component({
    selector: 'app-form',
    standalone: true,
    templateUrl: './form.component.html',
    styleUrl: './form.component.css',
    imports: [FooterComponent, FormsModule]
})
export class FormComponent {
    first_name: string = '';
    last_name: string = '';

    
}
