import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CastingDetailsComponent } from './casting-details.component';

describe('CastingDetailsComponent', () => {
  let component: CastingDetailsComponent;
  let fixture: ComponentFixture<CastingDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CastingDetailsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CastingDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
